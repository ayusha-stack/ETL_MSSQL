DROP TABLE IF EXISTS raw.one;
CREATE TABLE raw.one (
    name_employee varchar(50),
    dob varchar(20),
    location varchar(50),
    salary varchar(15),
    occupation varchar(50)
);

INSERT INTO raw.one (name_employee, dob, location, salary, occupation)
VALUES
    ('John Doe', '1985-03-15', 'New York', '75000', 'Software Engineer'),
    ('Jane Smith', '1990-08-22', 'Los Angeles', '62000', 'Marketing Specialist'),
    ('Michael Johnson', '1988-06-10', 'Chicago', '85000', 'Sales Manager'),
    ('Emily Williams', '1995-01-03', 'Houston', '56000', 'Administrative Assistant'),
    ('Robert Brown', '1982-11-28', 'Miami', '98000', 'Project Manager');
