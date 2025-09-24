import smtplib
import pandas as pd
import os
from email.message import EmailMessage

# Load email and file data
df = pd.read_excel(os.path.expanduser("~/Downloads/1.xlsx"), sheet_name="Sheet1")

# Email settings
smtp_server = "smtp.gmail.com"
smtp_port = 587
email_user = "markandrewbongon@gmail.com"  # lagay niyo here yung email address ng access
email_pass = "gtdf tlyb arcz peag"  # dito app password ng access. hindi to yung actual password ng email. search niyo sa google pano makuha

# Initialize server once
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(email_user, email_pass)

# Loop through each row and send email
for index, row in df.iterrows():
    name = str(row["Name"])
    committee = str(row["Committee"])
    # score = str(row["score"])
    recipient = row["Email"]

    msg = EmailMessage()
    msg["From"] = email_user
    msg["To"] = recipient
    msg["Subject"] = "Committee Placement - BUILDS Committee Membership Application"

    # Plain text fallback
    msg.set_content(
        "Thank you for joining BUILDS this Academic Year 2025-2026! Please read the full invitation using an HTML-supported mail client.")

    # HTML email content
    html_content = f"""
    <html lang="en">
    <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                @media screen and (max-width: 600px) {{
                .content {{
                    width: 100% !important;
                    display: block !important;
                    # padding: 10px !important;
                }}
                .header, .body, .footer {{
                    padding: 20px !important;
                }}
                h1 {{
                    font-size: 28px !important;
                    line-height: 36px !important;
                }}
                p {{
                    font-size: 16px !important;
                    line-height: 24px !important;
                }}
                img {{
                    width: 100% !important;
                    height: auto !important;
                }}
                }}

            </style>
        </head>
        <body style="margin:0;padding:0;font-family:'Poppins',Arial,sans-serif;">
    <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:#ffefe0;">
        <tr style ="height: 50px"></tr>
        <tr>
        <td align="center">
            <table role="presentation" class="content" width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width:800px;background:#ffffff;">

            <!-- Header -->
            <tr>
                <td align="center">
                <img src="https://lh3.googleusercontent.com/d/1uUuMIrogNOPR4b0et5DwKY5l44GEpeuo" 
                    alt="BUILDS Header" 
                    style="width:100%;max-width:800px;height:auto;display:block;" />
                </td>
            </tr>

            <!-- Body -->
            <tr>
                <td style="padding:24px;">
                <h1 style="font-size:38px;margin:15px 30px 20px 30px;font-family:Arial,sans-serif;text-align:center;">
                    Committee Placement - BUILDS Committee Membership Application
                </h1>
                <hr style="background:#feb063;height:1.5px;border:0;margin:0 30px 30px 30px;">
                <p style="margin:0 30px 20px 30px;font-size:20px;line-height:32px;text-align:justify;">
                    <b>Dear {name},</b><br><br>

                    First of all, congratulations and thank you for signing up to be part of our committee membership this academic year. We truly appreciate your willingness to contribute your skills, time, and energy in helping us fulfill our goals and serve the scholar community. <br><br>
                    In line with this, we are pleased to inform you that you have been placed as a committee member of the <b>{committee} Committee</b>. We are excited to see how you will bring value to your committee and the organization as a whole. <br><br>
                    To keep you updated and connected, please join our Main Committee Members Group Chat through this link:
                <!-- Group Chat Invite -->
                <div style="text-align:center; margin: 20px 0;">
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center">
        <tr>
        <td align="center" bgcolor="#F28C28" style="border-radius:8px;">
            <a href="https://m.me/j/AbYkgh3GnE8GRdPx/" 
            style="display:inline-block; background-color:#F28C28; color:#ffffff; 
                    padding:14px 28px; text-decoration:none; font-weight:bold; 
                    border-radius:6px; font-size:18px; font-family:Arial, sans-serif;">
            BUILDS Committee Members AY 2025-2026
            </a>
        </td>
        </tr>
    </table>
    </div>
                <p style="margin:0 30px 20px 30px;font-size:20px;line-height:32px;text-align:justify;">
                In the coming days, the separate group chats for each committee will also be created and managed by your respective committee heads. Kindly anticipate their invitations and stay tuned for further announcements.
    <br><br>
    Once again, congratulations and welcome to the BUILDS family of committee members! We look forward to working with you this year.
                    <br><br>
                    Should there be any concerns, feel free to reach out to us through this email or via Facebook through our official page: <a href="https://www.facebook.com/buildsofficial23">BUILDS Facebook Page</a> <br><br>
    Thank you very much!

                </p>
                <p style="font-size:20px;line-height:32px;margin:0 30px 20px 30px;">
                    Best regards, <br><br>
                    <b>JOHNRY E. ESPIRITU</b> <br>
                    <i>Internal Vice President</i> <br>
                    Bicol University Integrated League of DOST Scholars (BUILDS)<br>
                    Academic Year 2025-2026

                </p>
                </td>
            </tr>

          <!-- Footer -->
          <tr>
            <td style="background:#feb063;padding:16px;text-align:center;color:white;font-size:12px;">
              Bicol University Integrated League of DOST Scholars (BUILDS) | AY 2025-2026
            </td>
          </tr>

        </table>
      </td>
    </tr>
    <tr style ="height: 50px"></tr>
  </table>
</body>

</html>
"""

    msg.add_alternative(html_content, subtype="html")

    server.send_message(msg)
    print(f"Successfully emailed: {recipient}")

server.quit()
print("All emails sent successfully!")