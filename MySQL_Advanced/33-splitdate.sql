-- Selecting the split attribute and ordering by descending order
SELECT split
FROM metal_bands
WHERE split IS NOT NULL
ORDER BY split DESC
LIMIT 1;
