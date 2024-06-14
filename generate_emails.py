companies = [
    "Vidyard", "Recorded Future", "BambooHR", "Intercom", "Contently", "Tanium", 
    "Klaviyo", "LeadIQ", "Hosthub", "Cockroach Labs", "CloudTalk", "LuggageHero", 
    "Airlift", "Grab", "Airalo", "Undress", "Swvl", "Chipper Cash", "HqO", 
    "Porch Services", "Vivenu", "SendBird", "Mutiny", "BigID", "Clarifai", 
    "Socure", "DataRobot", "Algolia", "Bolt", "Iterable", "Fivetran", "Front", 
    "Snapdocs", "Snyk", "Lucid", "Sisense", "Lattice", "Miro", "Loom", 
    "Monday.com", "Notion", "Postman", "ServiceTitan", "Smartsheet", "Splashtop", 
    "Trello", "Zapier", "Zumper"
]


main_email_template = """
Hi {client_name},

Hope you're doing well. My name is Jake Mathew Sunil, and I’m passionate about learning. I recently came across {client_name} and was impressed by how it operates as a company.

I'm reaching out to see if there might be an opportunity for an internship with your team. I'm eager to learn and contribute, and I believe that working with {client_name} would be a great way to develop my skills.

Here’s what I can offer:
1. Willingness to Learn: I’m excited to learn from experienced professionals and am open to taking on any tasks that will help me grow.
2. Fresh Perspective: As someone new to the field, I can bring fresh ideas and a new perspective to your content.
3. Hard Work and Dedication: I’m committed to working hard and doing my best to contribute to your team’s success.
4. Basic Skills: I already have some experience with writing, SEO, and basic graphic design skills, and I’m ready to apply and build on these skills.

I’d be happy to start with a small project or even just shadow a team member to show you my enthusiasm and willingness to learn.

Are there any potential internship opportunities available? I’d love to learn more about how I can contribute to {client_name}.

Yours sincerely,

Jake Mathew Sunil

jakemathewsunil.com
"""

follow_up_email_template = """
Hi {client_name},

Hope you're well. I wanted to follow up on my previous email regarding an internship opportunity with {client_name}.

I’m really enthusiastic about the chance to learn and grow with your team. Please let me know if there are any potential opportunities available or if you have any questions.

Yours sincerely,

Jake Mathew Sunil

jakemathewsunil.com
"""

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cold Email Templates</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .email-section { margin-bottom: 40px; }
        button { margin-top: 10px; padding: 5px 10px; cursor: pointer; }
    </style>
</head>
<body>
    <h1>Cold Email Templates for Internship Opportunities</h1>
    <p>Click the buttons below each email to copy it to your clipboard.</p>
"""

# Function to create a button with a specific email content
def create_button(email_content):
    escaped_content = email_content.replace("`", "\\`").replace("\n", "\\n").replace("'", "\\'")
    return f"""
    <button onclick="copyToClipboard(`{escaped_content}`)">Copy to Clipboard</button>
    """

# Loop through each company and generate the email content
for company in companies:
    main_email = main_email_template.format(client_name=company).replace('\n', '<br>')
    follow_up_email = follow_up_email_template.format(client_name=company).replace('\n', '<br>')

    html_content += f"""
    <div class="email-section">
        <h2>{company}</h2>
        <h3>Main Email:</h3>
        <p>{main_email}</p>
        {create_button(main_email_template.format(client_name=company))}
        <h3>Follow-Up Email:</h3>
        <p>{follow_up_email}</p>
        {create_button(follow_up_email_template.format(client_name=company))}
    </div>
    """

# JavaScript function to copy email content to clipboard
html_content += """
<script>
function copyToClipboard(text) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand('copy');
    document.body.removeChild(textarea);
    alert('Email copied to clipboard');
}
</script>
</body>
</html>
"""

# Save the HTML content to a file
with open("Cold_Emails_for_Internship_Opportunities.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML file created successfully: Cold_Emails_for_Internship_Opportunities.html")
