# increasing ulimit
exec {'Changing Ulimit':
  path    => [ '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ],
  command => "sed -i 's/15/15000/g' /etc/default/nginx &&
  	     service nginx restart",
}