Use this script for creating an external dynamic data-group list on BIG-IP LTM and feed information about origin IPs from Azion CDN automatically. This script search for Azion Origin Shild list addresses specifically - used for control source IPs who can access your front end application.

### INSTRUCTIONS ###

1. Create a python file via bash on BIG-IP
2. Edit Authorization Header with your Azion credentials using URL Encode
```
[root@system1:Active:In Sync] ~ # echo 'user@domain:password' |base64
dXNlckBkb21haW46cGFzc3dvcmQK
```
4. Run the script to create a dynamic list
5. Import the external data group file using the following syntax: 
    * create /sys file data-group <imported_filename> separator "<separator>" source-path file:/<path_to_external_file> type <ip | string | integer>
      * Example: create sys file data-group ext_dg_azion_origin_shield source-path file:/root/ext_dg_azion_origin_shield.txt type ip
```
root@(system1)(cfg-sync In Sync)(Active)(/Common)(tmos)# create sys file data-group ext_dg_azion_origin_shield source-path file:/root/ext_dg_azion_origin_shield.txt type ip 
Copying file "file:/root/ext_dg_azion_origin_shield.txt" on route domain 0 ...
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  3907  100  3907    0     0  58.2M      0 --:--:-- --:--:-- --:--:-- 58.2M
root@(system1)(cfg-sync In Sync)(Active)(/Common)(tmos)# 
```
6. After you import the data group file, you can create the external data group. You specify the imported data group file when creating the external data group
7. Create an iRule to query your data-group list and associate it with one or more Virtual Severs. Follow example:
```
when CLIENT_ACCEPTED {
    if { ([class match [IP::client_addr] equals ext_dg_azion_origin_shield])}{
    } 
    else {
	    discard
    }
}
```

7. Create crontab entry to schedule dynamic list update via python script
