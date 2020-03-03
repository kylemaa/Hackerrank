<?php
// Import PHPMailer classes into the global namespace
// These must be at the top of your script, not inside a function
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

// Load Composer's autoloader
require 'vendor/autoload.php';
// Instantiation and passing `true` enables exceptions
$mail = new PHPMailer(true);

//If form submit
if (isset($_POST['submit'])) {

    //Validate the email the second time 
    if (filter_var($_POST['email'], FILTER_VALIDATE_EMAIL)) {

        $first_name = $_POST['first_name'];
        $last_name = $_POST['last_name'];
        $full_name = $first_name . " " . $last_name;
        $mail_from = $_POST['email'];
        $availability = $_POST['availability'];
        $pharmacy_npi = $_POST['NPI'];

        //Send to gmail
        $to ="";
        $toName = "";
        
        //Email subject
        $subject = "Potential Client";
        $messageHTML = "<strong>Name:</strong> " . $full_name . "<br/><strong>Email:</strong> " . $mail_from . "<br/>" . "<strong>Availability:</strong> " . $availability . "<br/>" . "<strong>Pharmacy & NPI:</strong> " . $pharmacy_npi;
        $messageAlt = "Name: " . $full_name . "\n" . "Email: " . $mail_from . "\n" . "Availability: " . $availability . "\n" . "Pharmacy & NPI: " . $pharmacy_npi;

        try {
            //Server settings
            //$mail->SMTPDebug = SMTP::DEBUG_SERVER;                      // Enable verbose debug output
            $mail->isSMTP();                                            // Send using SMTP
            $mail->Host       = 'smtp.gmail.com';                    // Set the SMTP server to send through
            $mail->SMTPAuth   = true;                                   // Enable SMTP authentication
            $mail->Username   = '';                     // SMTP username
            $mail->Password   = '';                               // SMTP password
            $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;         // Enable TLS encryption; `PHPMailer::ENCRYPTION_SMTPS` also accepted
            $mail->Port       = 587;                                    // TCP port to connect to

            //Recipients
            $mail->setFrom($mail_from, $full_name );
            $mail->addAddress($to, $toName);
            //$mail->addReplyTo($to, $toName);
            $mail->isHTML(true);                                  // Set email format to HTML
            $mail->Subject = $subject;
            $mail->Body    = $messageHTML;
            $mail->AltBody = $messageAlt;

            $mail->send();
            echo "<H1>Mail Sent. Thank you, " . $first_name . " we will get to your shortly!<H1>";
        } catch (Exception $e) {
            echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo}";
        }
        
    } else {
        echo "<H1>That is not a valid email! Please go back and check your fields<H1>";
    }
}
