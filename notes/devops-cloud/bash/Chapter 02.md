##  Programs & Commands 
### Identifying files

```bash
file $xyz
```
This command will tell me what kind of file the `xyz` file is exactly 

```bash
type -a $command
```
Find's what the source of any command

### Understanding PATH
It will look at each of the paths, present there, and execute the first one it finds
They are all separated by colon 
```shell
echo $PATH
# tr - translate, 
# '' - for backslash 
# \n - new line
echo $PATH | tr : '\n'
```
