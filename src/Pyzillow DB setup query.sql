
CREATE TABLE home_data (
    street_address INT NOT NULL PRIMARY KEY,
    zip INT NOT NULL,
    city VARCHAR(255),
    state VARCHAR(255),
    price DECIMAL(10 , 2 ),
    home_type VARCHAR(255),
    bedrooms INT,
    bathrooms INT,
    finished_sq_footage INT,
    lot_size_sq_footage INT,
    yearupdated INT,
    number_of_floors INT,
    parking_type VARCHAR(255),
    heating_sources VARCHAR(255),
    heating_system VARCHAR(255),
    floor_covering VARCHAR(255),
    rooms INT,
    neighborhood VARCHAR(255),
    shool_district VARCHAR(255)
)
/* The query sets up a MySQL table in whatever database it's executed against 
with the above attributes  - for PyZillow data pulled*/
