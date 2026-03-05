import arcpy

source1 = r"C:\Users\holde\OneDrive\Documents\GitHub\Diserens-online-GEOG676-spring2026-\Lab_7\landsat4"
band1 = arcpy.sa.Raster(source1 + r"\blue.tif")
band2 = arcpy.sa.Raster(source1 + r"\green.tif")
band3 = arcpy.sa.Raster(source1 + r"\red.tif")
band4 = arcpy.sa.Raster(source1 + r"\nir08.tif")
combined = arcpy.CompositeBands_management([band1, band2, band3, band4], source1 + r"\output_combined.tif")

source2 = r"C:\Users\holde\OneDrive\Documents\GitHub\Diserens-online-GEOG676-spring2026-\Lab_7\dem"

#hillshade
azimuth = 315
altitude = 45
shadows = 'NO_SHADOWS'
z_factor = 1
arcpy.ddd.HillShade(source2 + r"\dem_30m.tif", source2 + r"\output_Hillshade.tif", azimuth, altitude, shadows, z_factor)

#slope

output_measurment = "DEGREE"
z_factor = 1
arcpy.ddd.Slope(source2 + r"\dem_30m.tif", source2 + r"\output_Slop.tif", output_measurment, z_factor)
print("sucess!")