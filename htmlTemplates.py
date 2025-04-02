css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://imgs.search.brave.com/5x9NZt3m0oeOPIhX_BzqhQTE5spQYnKSmuhlwuzAzFs/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/cHJvZC53ZWJzaXRl/LWZpbGVzLmNvbS82/NjAwZTFlYWI5MGRl/MDg5YzJkOWM5Y2Qv/NjY2MWQwZTIxMGQy/Yzk2ZTA2YmNjNDdj/X0ZBRUJ0cmF1X2F0/NzdfMTAyNC53ZWJw" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://imgs.search.brave.com/Db8jYPRNkNYilq43ZMGU72y0YnCTcr4YlQ8HtYElCac/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9jZG4u/dGFsa2llLWFpLmNv/bS90YWxraWUtdXNl/ci1pbWcvMTQ1MDUx/NzQ0NjIwNjIwLzE2/Mzc0ODc2MTgwNTA0/Mi5qcGVnP3gtb3Nz/LXByb2Nlc3M9aW1h/Z2UvcmVzaXplLHdf/MTAyNC9mb3JtYXQs/d2VicA">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''