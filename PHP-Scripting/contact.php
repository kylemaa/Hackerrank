<?php 

//If form submit
if(isset($_POST['submit'])){
    
    //Validate the email the second time 
    if(filter_var($_POST['user[email]'], FILTER_VALIDATE_EMAIL)){  
        
        $first_name = $_POST['user[first_name]'];
        $last_name = $_POST['user[last_name]'];
        $mail_from = $_POST['user[email]'];
        $availability= $_POST['user[availability]'];
        $pharmacy_npi= $_POST['user[NPI]'];

        //Send to designated gmail
        $to ="";
        
        //Email subject
        $subject = "Potential Client";
        $message = "Name: ".$first_name." ".$last_name."\n"."Availability: ".$availability."\n"."Pharmacy & NPI: ".$pharmacy_npi;
        $headers = "From: ".$mail_from;
        //Mail function   
        if (mail($to,$subject,$message,$headers)){
            echo "<H1>Mail Sent. Thank you, ".$name." .We will get to your shortly!<H1>";
        }

        }else{ echo "Something went wrong :("; }
        
    }
        
    
?>