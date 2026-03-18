# Monitoring Scripts

## Scripts

| Script | Location | Runs Via | What It Does | Zabbix Item |
|--------|----------|----------|--------------|-------------|
| getLastStudies.py | local | task_scheduler | Checks latest dates on APWI database | .\db_dates.log|
| apwi_date_check.py | zabbix | zabbix system.run | Checks .85 for last consecutive radio file | smoo/APWI file check, smoo/APWI last date |
| portcheck.sh | zabbix | zabbix system.run | Runs nmap against current IP | Open Port Check, Current IP Address, Open Ports|
| Latest APWI db dates | local | task scheduler |APWI DB, outputs db_dates.log, FTPs to Zabbix | Latest apwi db dates | 
| ftpcheck.py | zabbix | zabbix system.run | Checks FTP file numbers | FTP Count Check | 
| ftpcheck_salem.py | zabbix | zabbix system.run | Check Salem FTP file numbers | FTP Salem Count Check |
| oneplace_feed_check.py | zabbix | zabbix system.run| Check feed.apwiradio.com scheduled podcasts | Oneplace Feed Monitor | 
| Mailchimp | zabbix | zabbix HTTP Agent  | Checks latest Mailchimp campaign (announcements) | Campaign Info | 

## Pipelines
### APWI DB Dates
1. `getLastStudies.py` runs locally via Task Scheudler — queries APWI DB, generates db_dates.log, FTPs to Zabbix server
2. Zabbix reads log via builtin `zabbix agent log[]` → item: "Latest apwi db dates"

## Templates
| Template | Related Scripts |
|----------|-----------------|
|apwi_missing_check.yaml | apwi_date_check.py
|Template Podcast Feed Monitor | oneplace_feed_check.py
|FTP File Count| ftpcheck.py, ftpcheck_salem.py

