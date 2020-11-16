#!/bin/bash
# 参数1=ip/域名 参数2=端口 参数3=控制执行 参数4=配置文件路径 参数5=nginx执行路径

valid_ip () {
    local  ip=$1
    local  stat=1

    if [[ $ip =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
        OIFS=$IFS
        IFS='.'
        ip=($ip)
        IFS=$OIFS
        [[ ${ip[0]} -le 255 && ${ip[1]} -le 255 \
        && ${ip[2]} -le 255 && ${ip[3]} -le 255 ]]
        stat=$?
    fi
    return $stat
}


#判断ip地址是否合法
if ! valid_ip "$1";then
    echo "IP不合法"
    exit 1
fi

cur_data=$(date +%Y%m%d%H%M%S)
bak_config='closeServer_'$4$cur_data

#鉴权
if [ x"$3" = x ]
then
 echo '缺少参数控制'
 exit 1
else
  #执行之前先备份原来的配置文件，避免出现问题
  cp $4 $bak_config
  sed -i "s/^\s*server\s*"$1":"$2"/    server "$1":"$2"/g" $4
  "$5" -s reload
  if (($? > 0))
  then
    echo 'start fail'
    if (($3 == 0))
    then
     ./closeServer.sh $1 $2 1
     "$5" -s reload
     echo 'huigun!!!!'
    fi
  else
    echo 'start success'
  fi
fi


