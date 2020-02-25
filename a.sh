for ((i=0;i<1000;i++));
do
echo "aaefawefwefawefefawef"|nc -u 104.194.206.222 9989 &
sleep 0.1
echo "go$i"
done
