-- 3. Old school band
-- all bands with Glam rock style
-- ranked by their longevity

SELECT 
    band_name,
        ifnull(split, YEAR(CURDATE())) - formed as lifespan
FROM metal_bands WHERE FIND_IN_SET('Glam rock', style)
ORDER BY lifespan DESC;
