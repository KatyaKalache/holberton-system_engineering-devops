# editing class-wp-locale.phpp name to .php
file { '/var/www/html/wp-setting.php':
 ensure => file,
} ->
exec { '/var/www/html/wp-setting.php':
  path => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
  command  => "sed -i 's/.phpp/.php/g' /var/www/html/wp-setting.php",