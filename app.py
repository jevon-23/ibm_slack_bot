import main
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.command("/find")
def handle_some_command(ack, body, logger, say):
    # Acknowledge that we are connecting to the bot  (tcp protocol i believe? )
    ack()

    # Find the command that was passed in that called our bot & error check
    command = body['command']
    if (command != '/find'):
        say(f"Bot should not be called")
        exit(-1)

    # Get the text that was passed in to the command, send it to our function 
    text = body['text']
    say(f"Searching for '{text}'")

    # Change the text into arguments
    argv = text.split(' ')
    argv = ['bot'] + argv

    # Run the main fn for the bot
    main.main(argv, say)

    logger.info(body)  

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
