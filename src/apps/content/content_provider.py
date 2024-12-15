from apps.shared.utils import read_markdown


class ContentProvider:
    def __init__(self, buddy_config):
        self.buddy_type_config = buddy_config
        self.system_content_version = self.buddy_type_config['system_content_version']
        self.user_content_version = self.buddy_type_config['user_content_version']

    @staticmethod
    def get_content_file_path(content_source, content_type, content_version):
        return f"apps/content/prompts/v{content_version}/{content_source}/{content_type}.md"

    def get_contents(self):
        content_source = self.buddy_type_config['name']
        system_content = read_markdown(self.get_content_file_path(content_source, 'system', self.system_content_version))
        user_content = read_markdown(self.get_content_file_path(content_source, 'user', self.user_content_version))
        return user_content, system_content
