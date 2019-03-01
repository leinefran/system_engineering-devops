# fix Apache return value
exec { 'fix wordpress extension':
    command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
    path    => '/bin'
}