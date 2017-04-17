<?php

require_once "vendor/autoload.php";
use \Dropbox as dbx;
use Symfony\Component\Yaml\Yaml;

function main ()
{
    try {
        $error = 0;
        $config = Yaml::parse(file_get_contents('config.yaml'));
        $uploaded_files = upload_files($config);
    } catch (Exception $e) {
        $error = $e->getMessage();
    } finally {
        $mail = new PHPMailer;
        
        $mail->isSMTP();                        // Set mailer to use SMTP
        $mail->Host = $config['mailHost'];      // Specify main and backup SMTP servers
        $mail->SMTPAuth = true;                 // Enable SMTP authentication
        $mail->Username = $config['sender'];    // SMTP username
        $mail->Password = $config['password'];  // SMTP password
        $mail->SMTPSecure = 'ssl';              // Enable TLS encryption, `ssl` also accepted
        $mail->Port = 465; 

        $mail->setFrom($config['sender'], 'I, Robot');
        $mail->addAddress($config['recipient']);    // Add a recipient

        $subj = 'Downloader';
        if ($error) {
            $subj .= ' - Error';
            $body = $error;
        } else {
            $subj .= ' - Ok';
            $body = var_export($uploaded_files, true);
        }
        $mail->Subject = $subj;
        $mail->Body    = $body;

        $exit_code = $mail->send();

        if (!$exit_code) {
            echo 'Message could not be sent.';
            echo 'Mailer Error: ' . $mail->ErrorInfo;
        } else {
            echo "Message has been sent\n";
        }

        return $exit_code;
    }
}

function upload_files ($config)
{
    $all_files = [];
    $dbxClient = new dbx\Client($config['accessToken'], "Downloader/0.1");

    foreach ($config['podcasts'] as $podcast) {
        echo $podcast['name'] .' '. $podcast['url'] ."\n";
        $new_files = get_url($dbxClient, $podcast['url'], $podcast['name']);
        if ($new_files) {
            $all_files[$podcast['name']] = $new_files;
        }
    }
    return $all_files;
}

function get_url ($dbxClient, $url, $dir)
{
    $sum_files = [];
    $rss = file_get_contents($url);
    preg_match_all('/https[^\"]+\.mp3/i', $rss, $matches);
    $urls = array_unique($matches[0]);
    
    if (! $dbxClient->getMetadata("/$dir")) {
        echo "create folder $dir\n";
        $dbxClient->createFolder("/$dir");
    }
    
    foreach ($urls as $file_url) {
        preg_match('/[^\/]+\.mp3/i', $file_url, $matches_2); 
        $file_name = $matches_2[0];
        echo "\n";
        echo "$file_name $file_url\n";
        $full_path = "/$dir/$file_name";
        $file_metadata = $dbxClient->getMetadata($full_path);
        echo "Check file: $file_name\t";
        if (! $file_metadata) {
            echo "Downloading ...\n";
            file_put_contents($file_name, fopen($file_url, 'r'));
            $f = fopen($file_name, 'rb');
            $result = $dbxClient->uploadFile($full_path, dbx\WriteMode::add(), $f);
            fclose($f);
            unlink($file_name);
            print_r($result);
            array_push($sum_files, $file_name);
        } else {
            echo "File exists\n";
        }
    }
    print_r($sum_files);
    return $sum_files;
}

main();

