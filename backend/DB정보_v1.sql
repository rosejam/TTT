-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema TTT
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema TTT
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `TTT` DEFAULT CHARACTER SET utf8 COLLATE utf8_bin ;
USE `TTT` ;

-- -----------------------------------------------------
-- Table `TTT`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TTT`.`user` (
  `pk` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(100) NOT NULL,
  `account_no` INT NULL,
  `account_bank` VARCHAR(45) NULL,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  PRIMARY KEY (`pk`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TTT`.`stock_market`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TTT`.`stock_market` (
  `pk` INT NOT NULL AUTO_INCREMENT COMMENT '주식의 고유 정보 컬럼이 추가될 수 있음',
  `stock_name` VARCHAR(45) NOT NULL,
  `stock_code` VARCHAR(45) NOT NULL,
  `status` INT NOT NULL DEFAULT 0 COMMENT '0이 기본, 정상',
  `market` INT NULL COMMENT 'kospi 0\nkostdaq 1\n',
  PRIMARY KEY (`pk`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TTT`.`log`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TTT`.`log` (
  `pk` INT NOT NULL AUTO_INCREMENT,
  `user_pk` INT NOT NULL,
  `timestamp` DATETIME NOT NULL DEFAULT current_timestamp,
  `buysell` VARCHAR(45) NOT NULL,
  `stock_pk` INT NOT NULL,
  `assets` BIGINT NULL,
  `balane` BIGINT NULL,
  INDEX `fk_log_user_idx` (`user_pk` ASC) VISIBLE,
  PRIMARY KEY (`pk`),
  INDEX `fk_log_stock1_idx` (`stock_pk` ASC) VISIBLE,
  CONSTRAINT `fk_log_user`
    FOREIGN KEY (`user_pk`)
    REFERENCES `TTT`.`user` (`pk`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_log_stock1`
    FOREIGN KEY (`stock_pk`)
    REFERENCES `TTT`.`stock_market` (`pk`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TTT`.`algorithm`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TTT`.`algorithm` (
  `pk` INT NOT NULL AUTO_INCREMENT,
  `user_pk` INT NOT NULL,
  PRIMARY KEY (`pk`),
  INDEX `fk_algorithm_user1_idx` (`user_pk` ASC) VISIBLE,
  CONSTRAINT `fk_algorithm_user1`
    FOREIGN KEY (`user_pk`)
    REFERENCES `TTT`.`user` (`pk`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `TTT`.`stock`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `TTT`.`stock` (
  `pk` INT NOT NULL AUTO_INCREMENT,
  `user_pk` INT NOT NULL,
  `stock_market_pk` INT NOT NULL,
  `stock_num` INT NULL,
  PRIMARY KEY (`pk`),
  INDEX `fk_stock_user1_idx` (`user_pk` ASC) VISIBLE,
  INDEX `fk_stock_stock_market1_idx` (`stock_market_pk` ASC) VISIBLE,
  CONSTRAINT `fk_stock_user1`
    FOREIGN KEY (`user_pk`)
    REFERENCES `TTT`.`user` (`pk`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_stock_stock_market1`
    FOREIGN KEY (`stock_market_pk`)
    REFERENCES `TTT`.`stock_market` (`pk`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
