import 'dart:isolate';
import 'dart:math';
import 'dart:io';

final int UPPER_BOUND = 1e8.toInt();

List<Isolate> isolates = [];

// number of primes will also be the number of times isolate.spawn is called
var primeNums = [3, 5, 7, 11, 13, 17, 31, 41];
var primes = new List<bool>.filled(UPPER_BOUND + 1, true);

class Values {
  int startInd;
  int endInd;
  List<bool> primes;

  Values(this.startInd, this.endInd, this.primes);
}

void SieveEmForGood(Values obj) {
  int res = sqrt(obj.endInd).toInt();
  for (int i = obj.startInd; i < res; i += 2) {
    if (obj.primes[i]) {
      // sieve to the upper bound
      for (int j = i * i; j < obj.endInd; j += i) {
        // cross it out!
        // The given index is not prime!
        obj.primes[j] = false;
      }
    }
  }
}

void start() async {
  for (var i = 0; i < primeNums.length; i++) {
    isolates.add(await Isolate.spawn(
        SieveEmForGood, new Values(primeNums[i], UPPER_BOUND, primes)));
  }
}

void stop() {
  for (Isolate i in isolates) {
    if (i != null) {
      i.kill(priority: Isolate.beforeNextEvent);
      i = null;
      print('Killed');
    }
  }
}

void main(List<String> args) async
{
  // var l = [1, 2, 3];
  // try {
  //   Iterable<int> it = l.getRange(0, 4);
  //   print(it);
  // } catch (e) {
  //   print(e);
  // }

  primes[0] = primes[1] = false;

  Stopwatch s = new Stopwatch()..start();

  await start();

  // print('Press enter to exit');
  // await stdin.first;

  stop();

  print('took ${s.elapsedMilliseconds} ms');

  var results = [2];
  int sum = 2;

  for (var i = 3; i < UPPER_BOUND; i+=2) {
    if (primes[i]) {
      results.add(i);
      sum += i;
    }
  }

  int len = results.length;

  print('number of prime numbers under 10^8: ${results.length}');
  print('total sum of all prime numbers under 10^8: ${sum}');

  print('ten largest primes: ${results.getRange(len - 10, len)}');

  print('done');
  stdin.first;
}
