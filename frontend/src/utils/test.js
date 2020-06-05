import { mapActions } from "vuex";

export default {

    // 전처리 함수
    preprocess(result) {
        result = result.substring(1, result.length-1);
        result = result.replace(/ /gi, "");   // replaceall과 같은 효과 - /와 / 사이에 있는 문자를 ""로 변환. g - 전부, i - 대소문자 구분 없이
        const resultList = result.split("}{");
        const result1 = resultList[0].split(",");
        const result2 = resultList[1].split(",");
        const result3 = resultList[2].split(",");
    
        // 포트폴리오1 데이터 초기화
        let chartData = [];
        for (let i = 0; i < result1.length; i++) {
            const r = result1[i].split(":");
            const date = r[0].substring(1, r[0].length-1).split("-");
            let d = new Date(date[0], date[1]-1, date[2], 0, 0).getTime()
    
            chartData.push([d, Number(r[1])]);
        }
        const p1 = chartData;
    
        // 포트폴리오2 데이터 초기화
        chartData = [];
        for (let i = 0; i < result2.length; i++) {
            const r = result2[i].split(":");
            const date = r[0].substring(1, r[0].length-1).split("-");
            let d = new Date(date[0], date[1]-1, date[2], 0, 0).getTime()
    
            chartData.push([d, Number(r[1])]);
        }
        const p2 = chartData;
    
        // 포트폴리오3 데이터 초기화
        chartData = [];
        for (let i = 0; i < result3.length; i++) {
            const r = result3[i].split(":");
            const date = r[0].substring(1, r[0].length-1).split("-");
            let d = new Date(date[0], date[1]-1, date[2], 0, 0).getTime()
    
            chartData.push([d, Number(r[1])]);
        }
        const p3 = chartData;

        return [p1, p2, p3];
    },
    
};
