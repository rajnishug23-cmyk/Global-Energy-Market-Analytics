SELECT MAX(year) AS latest_year
FROM dbo.new_energy_data;

SELECT COUNT(*) AS total_rows
FROM dbo.new_energy_data;

SELECT COUNT(DISTINCT country) AS number_of_countries
FROM dbo.new_energy_data;