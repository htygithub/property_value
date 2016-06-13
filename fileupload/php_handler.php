  protected function handle_file_upload($uploaded_file, $name, $size, $type, $error,
            $index = null, $content_range = null) {
        $file = new \stdClass();
		
		//HTY get unique fileID
		$orig_name=$name;
		$uniqid = $_POST['APPNAME'].'_' . uniqid();
		$name=$uniqid.'.'.pathinfo($name, PATHINFO_EXTENSION); //HTY
        $file->name = $this->get_file_name($uploaded_file, $name, $size, $type, $error,
            $index, $content_range);
        $file->size = $this->fix_integer_overflow(intval($size));
        $file->type = $type;
        if ($this->validate($uploaded_file, $file, $error, $index)) {
            $this->handle_form_data($file, $index);
            $upload_dir = $this->get_upload_path();
            if (!is_dir($upload_dir)) {
                mkdir($upload_dir, $this->options['mkdir_mode'], true);
            }
            $file_path = $this->get_upload_path($file->name);
            $append_file = $content_range && is_file($file_path) &&
                $file->size > $this->get_file_size($file_path);
            if ($uploaded_file && is_uploaded_file($uploaded_file)) {
                // multipart/formdata uploads (POST method uploads)
                if ($append_file) {
                    file_put_contents(
                        $file_path,
                        fopen($uploaded_file, 'r'),
                        FILE_APPEND
                    );
                } else {
                    move_uploaded_file($uploaded_file, $file_path);
                }
            } else {
                // Non-multipart uploads (PUT method support)
                file_put_contents(
                    $file_path,
                    fopen('php://input', 'r'),
                    $append_file ? FILE_APPEND : 0
                );
            }
            $file_size = $this->get_file_size($file_path, $append_file);
            if ($file_size === $file->size) {
                $file->url = $this->get_download_url($file->name);
                if ($this->is_valid_image_file($file_path)) {
                    $this->handle_image_file($file_path, $file);
                }
            } else {
                $file->size = $file_size;
                if (!$content_range && $this->options['discard_aborted_uploads']) {
                    unlink($file_path);
                    $file->error = $this->get_error_message('abort');
                }
            }
            $this->set_additional_file_properties($file);
        }
		
		//HTY change back to original filename to display
		$file->name=$orig_name;
		$file->complete="1";
		//htyinfo
		$txt = $_POST['APPNAME'].PHP_EOL.$_POST['APPNAME'].PHP_EOL.$_POST['email'].PHP_EOL.$orig_name.PHP_EOL.$_SESSION["APP_EXEC"].PHP_EOL.$_SESSION["APP_TYPE"].PHP_EOL.$_SESSION["id"].PHP_EOL;
		//Write info file for the uploaded data
		/*$myfile = fopen($file_path.".info", "w");
		
		
		fwrite($myfile, $txt);
		
		fclose($myfile);
		*/
		file_put_contents($file_path.".info", "\xEF\xBB\xBF".  $txt); 
		//file_put_contents($file_path.".info", $txt);
		
	/*	$array = [
					"APPNAME" 	=> $_POST['APPNAME'],
					"APP_EXEC" 	=> $_SESSION["APP_EXEC"],
					"APP_TYPE" 	=> $_SESSION["APP_TYPE"],
					"EMAIL"		=> $_POST['email'],
					"ORG_NAME"	=> $orig_name
				];
	
		
		//json_encode(array('phone_number' => '+33123456789'), JSON_NUMERIC_CHECK);
		$json_str=json_encode($array);
		$myfile = fopen($file_path.".json", "w");		
		
		fwrite($myfile, $json_str);
		
		fclose($myfile);
		*/
		
		
		
		
		
		
        return $file;
    }