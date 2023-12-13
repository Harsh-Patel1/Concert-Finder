CREATE DATABASE iwu_som_recordings;

CREATE TABLE Events (
    EventID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(255) NOT NULL,
    EventDate DATE NOT NULL,
    Program VARCHAR(255) --the file path to a program
    Poster VARCHAR(255) --file path to poster
)

CREATE TABLE Performances (
    PerformanceID INT PRIMARY KEY AUTO_INCREMENT,
    FOREIGN KEY (EventID) REFERENCES Events(EventID),
    FOREIGN KEY (WorkID) REFERENCES Works(WorkID),
    FOREIGN KEY (FileID) REFERENCES Files(FileID)
)

CREATE TABLE Files (
    FileID INT PRIMARY KEY AUTO_INCREMENT,
    Location VARCHAR(255) UNIQUE NOT NULL,
    FOREIGN KEY (EventID) REFERENCES Events(EventID),
    FOREIGN KEY (PerformanceID) REFERENCES Performances(PerformanceID)
)

CREATE TABLE Works (
    WorkID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(255) NOT NULL,
    Opus INT,
    Notes TEXT,
    DateWritten DATE NOT NULL,
    FOREIGN KEY (ComposerID) REFERENCES Composers(ComposerID)
)

CREATE TABLE Composers (
    ComposerID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(63) NOT NULL,
    MiddleName VARCHAR(63),
    LastName VARCHAR(63),
    Suffix VARCHAR(31),
    DateBorn DATE
)
