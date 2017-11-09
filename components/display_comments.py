# Please read in this order:
#   1. welcome.yaml
#   2. toggle_comment_collection.py
#   3. gather_text.yaml
#   4. check_settings.py
#   5. gather.py
#   6. gather_complete.yaml
#   7. display_comments.py
#
from meya import Component


class DisplayComments(Component):
    
    def start(self):
        
        # Check to see if the user is in the table. filter returns a list, so if
        # it's length is greater than 0, our user has a record.
        if len(self.db.table("comments").filter(user_id__contains=self.db.user.id)) == 0:
            return self.respond(message=self.create_message(text="User does not exist!"), action="next")
        
        # Concatenate all comments. Notice the `-` before `comment_id`. This
        # sorts the comment_ids from highest to lowest.
        comments = self.db.table("comments").filter(user_id=self.db.user.id, order_by=["comment_id"])[1:]

        text = ""
        for comment in comments:
            print comment
            text += comment["text"] + "\n"
        
        # Display the text and return to the flow that called this conponent.
        message = self.create_message(text=text)
        return self.respond(message=message, action="next")