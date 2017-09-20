# increasing the number of worker processses to 7
exec {'/etc/nginx/nginx.conf':
  path    => [ '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ],
  command => "sed -i 's/worker_processes 4;/worker_processes 7;/g' /etc/nginx/nginx.conf",
}

exec {'restart nginx after editing congfig file':
  path    => [ '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ],
  command => "service nginx restart"
}