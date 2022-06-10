Use this script for creating an external dynamic data-group list on BIG-IP LTM and feed information about origin IPs from Azion CDN automatically. This script search for Azion Origin Shild list addresses specifically - used for control source IPs who can access your front end application.

### INSTRUCTIONS ###

1. Create file via bash on BIG-IP
2. Edit Authorization Header with your Azion credentials using URL Encode (ex: echo 'user@domain:password' |base64)
3. Run the script to create a dynamic list
4. Import the external data group file using the following syntax: 
    * create /sys file data-group <imported_filename> separator "<separator>" source-path file:/<path_to_external_file> type <ip | string | integer>
      * Example: create sys file data-group ext_dg_azion_origin_shield source-path file:/var/tmp/ext_dg_azion_origin_shield.txt type ip
5. After you import the data group file, you can create the external data group. You specify the imported data group file when creating the external data group
6. Create crontab entry to schedule dynamic list update via python script
