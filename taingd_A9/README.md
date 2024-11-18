## Job Explanations
- 0 2 * * * rm \~/path/to/home/temp/*
	Deletes all files from a specified folder (replace "\~/path/to/home/temp/*" with the folder you want to delete from) everyday at 2AM.

- 0 3 * * 0 tar -czf ~/path/to/home/user/backups/backupTest.tar.gz ~/path/to/home/user/*
	Backs up the specified folder (replace "\~/path/to/home/user/*" with the folder you want to backup ) to \~/path/to/home/user/backups/backupTest.tar.gz (replace "backupTest" with whatever you want the backup to be named) every Sunday at 3AM.

- 30 8 * * * echo \`df -h\` | mail -s "Disk usage report" temp@CS131.com
	Emails a disk usage report (output of "df - h") to a specified email (replace "temp@CS131.com" with your email) every day at 8:30AM.


## How To Use Crontab
- To use the jobs above, it is necessary to edit your crontab file, which is where all your cron jobs are stored.
- Type "crontab -e" in your terminal window.
- Paste the contents of "crontab_copy.txt" into the crontab.
- Save and exit the file.
