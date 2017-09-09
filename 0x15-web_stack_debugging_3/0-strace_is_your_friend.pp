# editing class-wp-locale.phpp name to .php
exec { '/var/www/html/wp-setting.php':
  path => [ '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ],
  command  => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}