# Project: 0x03. Log Parsing

## Content

## Script reads stdin line by line and computes metrics:

### Input format: - [] "GET /projects/260 HTTP/1.1" (if the format is not this one, the line must be skipped)
### After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
### Number of lines by status code:
#### possible status code: 200, 301, 400, 401, 403, 404, 405 and 500

| Task | File |
| ---- | ---- |
| 0. Log parsing | [0-stats.py](./0-stats.py) |
