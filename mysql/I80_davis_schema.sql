

CREATE TABLE IF NOT EXISTS `I80_davis_t` 
(
    -- `id` INT NOT NULL AUTO_INCREMENT,
    `timestamp` TEXT NOT NULL,
    `ID` INT NOT NULL,
    `avg_speed` INT DEFAULT NULL,
    `avg_flow` INT DEFAULT NULL,
    `avg_occ` INT DEFAULT NULL,
    `avg_freeflow_speed` INT DEFAULT NULL,
    `samples_below_100pct_ff` INT DEFAULT NULL,
    `samples_below_95pct_ff` INT DEFAULT NULL,
    `samples_below_90pct_ff` INT DEFAULT NULL,
    `samples_below_85pct_ff` INT DEFAULT NULL,
    `samples_below_80pct_ff` INT DEFAULT NULL,
    `samples_below_75pct_ff` INT DEFAULT NULL,
    `samples_below_70pct_ff` INT DEFAULT NULL,
    `samples_below_65pct_ff` INT DEFAULT NULL,
    `samples_below_60pct_ff` INT DEFAULT NULL,
    `samples_below_55pct_ff` INT DEFAULT NULL,
    `samples_below_50pct_ff` INT DEFAULT NULL,
    `samples_below_45pct_ff` INT DEFAULT NULL,
    `samples_below_40pct_ff` INT DEFAULT NULL,
    `samples_below_35pct_ff` INT DEFAULT NULL,
    `samples_below_30pct_ff` INT DEFAULT NULL,
    `samples_below_20pct_ff` INT DEFAULT NULL,
    `samples_below_25pct_ff` INT DEFAULT NULL,
    `samples_below_15pct_ff` INT DEFAULT NULL,
    `samples_below_10pct_ff` INT DEFAULT NULL,
    -- PRIMARY KEY (`ID`)

)
-- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `richards` 
(
    `id` INT NOT NULL AUTO_INCREMENT,
    `timestamp` TEXT NOT NULL,
    `flow1` INT NOT NULL,
    `occupancy1` FLOAT DEFAULT NULL,
    `flow2` INT DEFAULT NULL,
    `occupancy2` INT DEFAULT NULL,
    `flow3` INT DEFAULT NULL,
    `occupancy3` FLOAT DEFAULT NULL,
    `totalflow` INT DEFAULT NULL,
    `weekday` INT DEFAULT NULL,
    `hour` INT DEFAULT NULL,
    `minute` INT DEFAULT NULL,
    `second` INT DEFAULT NULL,
    -- PRIMARY KEY (`id`)
    -- FOREIGN KEY (`timestamp`) REFERENCES I80_davis(`timestamp`)

)
-- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `station_summary` 
(
    -- `id` INT NOT NULL AUTO_INCREMENT,
    `ID` TEXT NOT NULL,
    `flow_99 flow_max` INT NOT NULL,
    `flow_median` INT DEFAULT NULL,
    `flow_total` FLOAT DEFAULT NULL,
    `n_obs` INT DEFAULT NULL,
   
    -- PRIMARY KEY (`id`)
    -- FOREIGN KEY (`ID`) REFERENCES I80_davis(`ID`)

)
-- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `weekday` 
(
    -- `id` INT NOT NULL AUTO_INCREMENT,
    `ID` TEXT NOT NULL,
    `hour` INT NOT NULL,
    `second` INT DEFAULT NULL,
    `Unnamed_4` FLOAT DEFAULT NULL,
    `totalflow` INT DEFAULT NULL,


   
    -- PRIMARY KEY (`id`)
    -- FOREIGN KEY (`ID`) REFERENCES I80_davis(`ID`)

)
-- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `I80_stations` 
(
    -- `id` INT NOT NULL AUTO_INCREMENT,
    `ID` TEXT NOT NULL,
    `Fwy` INT NOT NULL,
    `Dir` VARCHAR(10) DEFAULT NULL,
    `District` INT DEFAULT NULL,
    `County` INT DEFAULT NULL,
    `City` INT DEFAULT NULL,
    `State_PM` FLOAT DEFAULT NULL,
    `Abs_PM` FLOAT DEFAULT NULL,
    `Latitude` FLOAT DEFAULT NULL,
    `Longitude` FLOAT DEFAULT NULL,
    `Length` FLOAT DEFAULT NULL,
    `Type` VARCHAR(10) DEFAULT NULL,
    `Lanes` INT DEFAULT NULL,
    `Name` VARCHAR(100) DEFAULT NULL,
    `User_ID_1` VARCHAR(100) DEFAULT NULL,
    `User_ID_2` VARCHAR(100) DEFAULT NULL,
    `User_ID_3` VARCHAR(100) DEFAULT NULL,
    `User_ID_4` VARCHAR(100) DEFAULT NULL,
    
    -- PRIMARY KEY (`id`)
    -- FOREIGN KEY (`ID`) REFERENCES I80_davis(`ID`)

)
-- ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `I80_median` 
(
    -- `id` INT NOT NULL AUTO_INCREMENT,
    `ID` TEXT NOT NULL,
    `weekday` TEXT NOT NULL,
    `hour` TEXT NOT NULL,
    `minute` TEXT NOT NULL,
    `second` TEXT NOT NULL,
    `flow1` FLOAT DEFAULT NULL,
    `occupancy1` FLOAT DEFAULT NULL,
    `mph1` FLOAT DEFAULT NULL,
    `flow2` FLOAT DEFAULT NULL,
    `occupancy2` FLOAT DEFAULT NULL,
    `mph2` FLOAT DEFAULT NULL,
    `flow3` FLOAT DEFAULT NULL,
    `occupancy3` FLOAT DEFAULT NULL,
    `mph3` FLOAT DEFAULT NULL,
    `flow4` FLOAT DEFAULT NULL,
    `occupancy4` FLOAT DEFAULT NULL,
    `mph4` FLOAT DEFAULT NULL,
    `flow5` FLOAT DEFAULT NULL,
    `occupancy5` FLOAT DEFAULT NULL,
    `mph5` FLOAT DEFAULT NULL,
    `totalflow` FLOAT DEFAULT NULL,


    -- PRIMARY KEY (`id`)
    -- FOREIGN KEY (`ID`) REFERENCES I80_davis(`ID`)

)
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE utf8mb4_unicode_ci;
