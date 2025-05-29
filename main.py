from core.config_loader import ConfigLoader

def main():
    config_path = "config/config.xml"

    try:
        config_loader = ConfigLoader(config_path)
        settings = config_loader.get_settings()
        print('configuration loaded successfully:')
        print(settings)

    except Exception as e:
        print(f'Failed to load configuration: {e}')

if __name__ == '__main__':
    main()
