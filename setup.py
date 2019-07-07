from distutils.core import setup

pkg = 'Extensions.Biscotto'
setup (name = 'enigma2-plugin-extensions-Biscotto',
       version = '2.0-r2',
       description = 'Add BISS, PowerVU, IRDETO and Tandberg key to current service',
       packages = [pkg],
       package_dir = {pkg: 'plugin'},
       package_data = {pkg: ['plugin.png']},
      )
