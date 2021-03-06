import dataproc.configargparse
import appdirs

def test_appdir():
    p = dataproc.configargparse.get_argument_parser(name='test_cap', appdir_conf=True)
    #p = configargparse.ArgParser(appdir_conf=True)

def test_base():
    p = dataproc.configargparse.ArgParser(appdir_conf=True)
    #p.add('-c', '--my-config', required=True, is_config_file=True, help='config file path')
    p.add('--genome', required=False,
          help='path to genome file')  # this option can be set in a config file because it starts with '--'
    p.add('-v', help='verbose', action='store_true')
    p.add('-d', '--dbsnp', help='known variants .vcf',
          env_var='DBSNP_PATH')  # this option can be set in a config file because it starts with '--'
    p.add('vcf', nargs='+', help='variant file(s)')

    options = p.parse_args()

    print(options)
    print(p.format_help())
    print(p.format_values())  # useful for logging where different settings came from
