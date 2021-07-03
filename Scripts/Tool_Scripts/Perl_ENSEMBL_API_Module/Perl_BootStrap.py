#"http://m.ensembl.org/info/docs/api/api_git.html"
import subprocess

var = "/some/file/path/"
pipe = subprocess.Popen(["perl", "Perl_Main.pl", var], stdin=subprocess.PIPE)
pipe.stdin.write(var.encode())
pipe.stdin.close()