## Uaa 小说下载解析器

[原网站uaa.com](https://www.uaa.com/)

配置项`.config.json`

- json_file_path           下载的json文件存储位置
- db_file_path             数据库文件的存储位置
- is_remove_jsonfile       是否在下载完成后删除json文件

如下

```json
{
  "json_file_path": "./JsonDownload",
  "db_file_path": "./UaaDb.db",
  "is_remove_jsonfile": false
}
```