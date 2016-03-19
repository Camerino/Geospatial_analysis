import urllib
import os
from osgeo import osr

def create_epsg_wkt_esri(epsg):
    spatial_ref = osr.SpatialReference()
    spatial_ref.ImportFromEPSG(epsg)
    spatial_ref.MorphToESRI()

    wkt_epsg = spatial_ref.ExportToWkt()

    return wkt_epsg

def write_prj_file(foldername, shp_filename, epsg):
    in_shp_name = "{0}.prj".format(shp_filename)
    full_path_name = foldername + in_shp_name

    with open(full_path_name, "w") as prj:
        epsg_code = create_epsg_wkt_esri(epsg)
        prj.write(espg_code)
        print "done writing projection definition: " + epsg_code

def run_batch_define_prj(folder_location, epsg):
    shapefile_list = []

    for shp_file in os.listdir(folder_location):
        if shp_file.endwith('.shp'):
            filename_no_ext = os.path.splitext(shp_file)[0]
            shapefile_list.append(filename_no_ext)

    for shp in shapefile_list:
        write_prj_file(folder_location, shp, epsg)
        
