# coding: utf-8

# Function for calculating windspeed from U and V components
# Author - luke.sanger@wemcouncil.org
# June 2019

# IMPORTANT: takes U and V files as input, also define location for the WS output

def wsFunc(ufile,vfile,outpath):

    # load packages
    import iris
    import os

    # strip filepath from filename for naming purposes
    ufilename = os.path.basename(ufile)
    vfilename = os.path.basename(vfile)

    # set wind height resolution for loop
    var1 = '0010m'
    var2 = '0100m'

    # add files to list
    filenames = [ufile,vfile]

    # load u and v components as list of cubes
    cubes = iris.load(filenames)
    ucube = cubes[0]
    vcube = cubes[1]

    # if 10m is in filename then do this:
    if var1 in ufilename and vfilename:

        ds1 = ucube
        ds2 = vcube

        # calculate ws
        ds12 = ds1
        ds12.data = (ds1.data**2 + ds2.data**2)**(1/2)
        
        # rename variable to uv
        ds12.rename('10 Metre Wind Speed')
        
        # construct filename for WS output
        filename = outpath + ufilename[:17] + 'WS-' + ufilename[20:]
        
        # save ws as .nc to outpath
        iris.fileformats.netcdf.save(ds12, filename, netcdf_format='NETCDF4')

    # if 100m is in filename then do this:
    elif var2 in ufilename and vfilename:

        ds3 = ucube
        ds4 = vcube

        # calculate ws
        ds34 = ds3
        ds34.data = (ds3.data**2 + ds4.data**2)**(1/2)
        
        # rename variable to uv
        ds34.rename('100 Metre Wind Speed')
        
        # construct filename for WS output
        filename2 = outpath + ufilename[:17] + 'WS-' + ufilename[20:]

        # save ws as .nc to outpath
        iris.fileformats.netcdf.save(ds34, filename2, netcdf_format='NETCDF4')

