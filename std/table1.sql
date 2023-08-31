CREATE schema std;
CREATE TABLE std.one(
    name_employee varchar(),
    dob date(),
    location varchar(),
    salary float,
    occupation varchar ()
);
INSERT INTO std.one(
    name_employee,
    dob,
    location,
    salary,
    occupation
)
SELECT
    name_employee,
    dob::date,
    location,
    salary::float,
    occupation
FROM raw.one;