# ibm_slack_bot
Uses web scraping to return back information on [Data Areas](https://www.ibm.com/docs/en/zos/2.2.0?topic=zm-zos-v2r2-mvs-data-areas-volume-1-abe-iax) 
for the IBM z/OS machine <br> <br>

# Getting the bot up and running
For usage, first we need to activate the python environment <br>
```source ./.venv/bin/activate```
<br>

Next save the environment variables for your app and the bot <br>

```export SLACK_BOT_TOKEN='xoxb-...'``` <br>
```export SLACK_APP_TOKEN='xapp-...'``` <br>

Now the environment is set up, to spin up the bot run <br> <br>

Using Docker:<br><br>
```docker compose up```
<br><br>
Commandline:<br><br>
```python3 app.py```

Bot is now up and running. To interact with the bot, go to a workspace that you share with the bot and run /find.
<br> <br>

# Interacting with the bot
Usage:
```
/find {control_block} info -> returns what sections of info is block has
  /find ascb info 
/find {control_block} inter -> Returns Programming Interface Information
  /find ascb inter 
/find {control_block} head -> Returns the heading information 
  /find ascb head
/find {control_block} map -> Returns back the entire mapping of this control_block
  /find ascb map

/find {control_block} head {row_name} -> Returns a specific row out of head w/ the key value ROW_NAME
  /find ascb head common
/find {control_block}  map {row_name} -> Returns back the row of this control_blocks' mapping associated w/ ROW_NAME
  /find ascb  map ascbascb 
/find {control_block}  map {dec_offset} -> Returns back the row that has the decimal offset DEC_OFFSET
  /find ascb map 20
/find {control_block} map -x{hex_offset} -> Returns back the row that has the hex offset of HEX_OFFSET
  /find ascb map -x20
  
```
