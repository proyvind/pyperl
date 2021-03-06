import perl
import sys

print("1..4")

perl.eval("use lib 't'")     # good when running from ..
perl.eval("use TestClass")

try:
	obj = perl.callm("new", "NotAClass")
except perl.PerlError as v:
	expect = "Can't locate object method \"new\" via package \"NotAClass\""
	if str(v)[:len(expect)] != expect:
		print("not", end=' ')
	print("ok 1")

obj = perl.callm("new", "TestClass")

try:
	obj.not_a_method(34, 33);
except perl.PerlError as v:
	if str(v) != "Can't locate object method \"not_a_method\" via package \"TestClass\".\n":
		print("not", end=' ')
	print("ok 2")
except AttributeError:
	if not perl.MULTI_PERL:
		print("not", end=' ')
	print("ok 2")

try:
	obj.error("foo");
except perl.PerlError as v:
	if str(v)[:15] != "Failed: foo at ": print("not", end=' ')
	print("ok 3")
except AttributeError:
	if not perl.MULTI_PERL:
		print("not", end=' ')
	print("ok 3")

try:
	perl.eval("{}").xyzzy()
except AttributeError as v:
	from string import find
	if find(str(v), "xyzzy") == -1:
		#print v
		print("not", end=' ')
	print("ok 4")
