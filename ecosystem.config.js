module.exports = {
  apps : [{
    name: __dirname.split('/').pop(),
    script: 'server.py',
    args: '',
    autorestart: true,
    log_date_format: 'HH:mm:ss',
    watch: true,
    ignore_watch : [".git", "__pycache__", "data.json", "data.tmp.json"],
    max_memory_restart: '2G',
  }]
};