-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema cookies
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cookies
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cookies` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
-- -----------------------------------------------------
-- Schema Assignment8
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Assignment8
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Assignment8` ;
-- -----------------------------------------------------
-- Schema assignment8
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema assignment8
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `assignment8` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `cookies` ;

-- -----------------------------------------------------
-- Table `cookies`.`patients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cookies`.`patients` (
  `PatientsID` INT NOT NULL AUTO_INCREMENT,
  `FirstName` VARCHAR(45) NOT NULL,
  `LastName` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`PatientsID`))
ENGINE = InnoDB
AUTO_INCREMENT = 1000002
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `cookies`.`visits`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cookies`.`visits` (
  `VisitsDate` VARCHAR(45) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_0900_ai_ci' NULL DEFAULT NULL,
  `VisitsID` VARCHAR(45) CHARACTER SET 'utf8mb4' COLLATE 'utf8mb4_0900_ai_ci' NULL DEFAULT NULL,
  `PatientID` INT NULL DEFAULT NULL,
  INDEX `FK_PatientID_idx` (`PatientID` ASC) VISIBLE,
  CONSTRAINT `FK_PatientID`
    FOREIGN KEY (`PatientID`)
    REFERENCES `cookies`.`patients` (`PatientsID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;

USE `Assignment8` ;

-- -----------------------------------------------------
-- Table `Assignment8`.`Patient`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Assignment8`.`Patient` (
  `PatientID` INT NOT NULL AUTO_INCREMENT,
  `FirstName` VARCHAR(45) NOT NULL,
  `LastName` VARCHAR(45) NOT NULL,
  `InsuranceProvider` VARCHAR(45) NOT NULL,
  `InsuranceID` INT NOT NULL,
  `Address` VARCHAR(45) NOT NULL,
  `Phone` INT NOT NULL,
  `PaymentMethod` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`PatientID`, `InsuranceProvider`, `InsuranceID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Assignment8`.`Insurance`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Assignment8`.`Insurance` (
  `InsuranceID` INT NOT NULL,
  `Copay` VARCHAR(45) NULL,
  `PatientID` INT NULL,
  INDEX `FK_PatientID_idx` (`PatientID` ASC) VISIBLE,
  INDEX `FK_InsuranceID_idx` (`InsuranceID` ASC) VISIBLE,
  CONSTRAINT `FK_InsuranceID`
    FOREIGN KEY (`InsuranceID`)
    REFERENCES `Assignment8`.`Patient` (`InsuranceID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_PatientID`
    FOREIGN KEY (`PatientID`)
    REFERENCES `Assignment8`.`Patient` (`PatientID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Assignment8`.`Payment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Assignment8`.`Payment` (
  `PatientID` INT NOT NULL,
  `Method` VARCHAR(45) NOT NULL,
  `InsuranceID` INT NULL,
  PRIMARY KEY (`PatientID`),
  INDEX `FK_InsuranceID_idx` (`InsuranceID` ASC) VISIBLE,
  CONSTRAINT `FK_PatientID`
    FOREIGN KEY (`PatientID`)
    REFERENCES `Assignment8`.`Patient` (`PatientID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `FK_InsuranceID`
    FOREIGN KEY (`InsuranceID`)
    REFERENCES `Assignment8`.`Patient` (`InsuranceID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

USE `assignment8` ;

-- -----------------------------------------------------
-- Table `assignment8`.`patients`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `assignment8`.`patients` (
  `PatientID` INT NOT NULL AUTO_INCREMENT,
  `FirstName` VARCHAR(45) NOT NULL,
  `LastName` VARCHAR(45) NOT NULL,
  `InsuranceProvider` VARCHAR(45) NOT NULL,
  `Address` VARCHAR(45) NULL DEFAULT NULL,
  `Phone` INT NULL DEFAULT NULL,
  `Email` VARCHAR(45) NULL DEFAULT NULL,
  `PhysicianID` INT NOT NULL,
  PRIMARY KEY (`PatientID`, `PhysicianID`, `InsuranceProvider`),
  INDEX `FK_InsuranceProvider` (`InsuranceProvider` ASC) VISIBLE,
  INDEX `FK_PhysicianID` (`PhysicianID` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `assignment8`.`appointment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `assignment8`.`appointment` (
  `PatientID` INT NOT NULL,
  `AppointmentID` INT NOT NULL,
  `PhysicianID` INT NOT NULL,
  `ReasonForVisit` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`PatientID`),
  INDEX `FK_PhysicianID_idx` (`PhysicianID` ASC) INVISIBLE,
  CONSTRAINT `FK2_PatientID`
    FOREIGN KEY (`PatientID`)
    REFERENCES `assignment8`.`patients` (`PatientID`),
  CONSTRAINT `FK_PhysicianID`
    FOREIGN KEY (`PhysicianID`)
    REFERENCES `assignment8`.`patients` (`PhysicianID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `assignment8`.`payment`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `assignment8`.`payment` (
  `PatientID` INT NOT NULL,
  `Method` VARCHAR(45) NOT NULL,
  `InsuranceID` INT NOT NULL,
  `InsuranceProvider` VARCHAR(45) NOT NULL,
  `Copay` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`PatientID`, `InsuranceProvider`),
  INDEX `FK_InsuranceProvider_idx` (`InsuranceProvider` ASC) INVISIBLE,
  CONSTRAINT `FK_InsuranceProvider`
    FOREIGN KEY (`InsuranceProvider`)
    REFERENCES `assignment8`.`patients` (`InsuranceProvider`),
  CONSTRAINT `FK_PatientID`
    FOREIGN KEY (`PatientID`)
    REFERENCES `assignment8`.`patients` (`PatientID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;

USE `Assignment8` ;

-- -----------------------------------------------------
--  routine1
-- -----------------------------------------------------

DELIMITER $$
USE `Assignment8`$$
$$

DELIMITER ;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
