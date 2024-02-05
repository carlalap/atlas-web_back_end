-- 3. Old school band
-- all bands with Glam rock style
-- ranked by their longevity

SELECT 
    band_name,
        ifnull(split, 2020) - formed as lifespan
FROM metal_bands WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
