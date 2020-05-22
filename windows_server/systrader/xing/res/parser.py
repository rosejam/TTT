import json
import logging
import os
import re
import shutil

import tslib.xing
import settings

__author__ = 'Moon Kwon Kim'

import pandas as pd
import pickle

logger = logging.getLogger(__name__)


XING_RES_BASE = os.path.dirname(os.path.abspath( __file__ ))


def _parse(res, mode=0, blocks=None, occurs=None, name=None, prefix=None):
    for line in res:
        tokens = re.split(r"[,]", re.sub('[\s+;]', '', line))
        if mode == 0 and tokens[0].startswith("."):
            return _parse(res, mode=0, blocks={}, occurs=[], prefix=tokens[2])
        elif mode == 0 and tokens[0] == "BEGIN_DATA_MAP":
            return _parse(res, mode=1, blocks={}, occurs=[], prefix=prefix)
        elif mode == 1 and tokens[0] == "END_DATA_MAP":
            return blocks, occurs
        elif mode == 1:
            name = tokens[0]
            # if name.startswith("InBlock") or name.startswith("OutBlock"):
            if "InBlock" in name or "OutBlock" in name:
                if prefix not in name:
                    name = prefix+name
                if "OutBlock" in name and tokens[-1].rstrip(';') == "occurs":
                    occurs.append(name)
            return _parse(res, mode=2, blocks=blocks, occurs=occurs, name=name, prefix=prefix)
        elif mode == 2 and tokens[0] == "begin":
            continue
        elif mode == 2 and tokens[0] == "end":
            return _parse(res, mode=1, blocks=blocks, occurs=occurs, prefix=prefix)
        elif mode == 2:
            if name not in blocks:
                blocks[name] = []
            blocks[name].append(tokens)


def parse(res_name):
    with open(os.path.join(tslib.xing.XING_RES_PATH, res_name), 'r') as res:
        return _parse(res)


def export_all():
    blocks = {}
    occurs = []
    # shutil.rmtree("./blocks")
    # os.mkdir("./blocks")
    for res_name in os.listdir(tslib.xing.XING_RES_PATH):
        if re.match(r"^.*(?!_\d).{2}\.res$", res_name):
            _blocks, _occurs = parse(res_name)
            for name, data in _blocks.items():
                data = pd.DataFrame(data)
                # data.to_csv("./blocks/%s.csv" % name, encoding="utf-8", index=False, header=False)
                blocks[name] = data
            if _occurs is not None and len(_occurs) > 0:
                occurs.extend(_occurs)

    with open(os.path.join(XING_RES_BASE, 'blocks.pickle'), 'wb') as f:
        pickle.dump(blocks, f)
        f.close()
    with open(os.path.join(XING_RES_BASE, 'occurs.pickle'), 'wb') as f:
        pickle.dump(occurs, f)
        f.close()

    return blocks, occurs


def import_all():
    blocks = None
    occurs = None
    if os.path.isfile(os.path.join(XING_RES_BASE, 'blocks.pickle')):
        with open(os.path.join(XING_RES_BASE, 'blocks.pickle'), 'rb') as f:
            blocks = pickle.loads(f.read())
            f.close()
    if os.path.isfile(os.path.join(XING_RES_BASE, 'occurs.pickle')):
        with open(os.path.join(XING_RES_BASE, 'occurs.pickle'), 'rb') as f:
            occurs = pickle.loads(f.read())
            f.close()
    return blocks, occurs

    # res = {}
    # path = os.path.join(os.path.dirname(__file__), "blocks")
    # if not os.path.exists(path):
    #     os.makedirs(path)
    # for csv in os.listdir(path):
    #     try:
    #         res[re.sub("\.csv", "", csv)] = pd.read_csv(os.path.join(path, csv), encoding="utf-8", index_col=False, header=None)
    #     except:
    #         logger.debug("No content in %s" % csv)
    # return res


def import_block(bname):
    path = os.path.join(os.path.dirname(__file__), "blocks.pickle")
    path = os.path.join(path, bname+".csv")
    return pd.read_csv(path, encoding="utf-8", index_col=False, header=None)


if __name__ == '__main__':
    export_all()
    # blocks, occurs = import_all()
    # print(blocks)
    # print(occurs)
