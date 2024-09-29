type Callback = (...args: any[]) => any;
type Subscription = {
  unsubscribe: () => void;
};

/*
 {
    firstEvent: [cb1, cb2],
 }

 */

class EventEmitter {
  eventMap: Record<string, Callback[]> = {};

  subscribe(eventName: string, callback: Callback): Subscription {
    if (eventName in this.eventMap) {
      this.eventMap[eventName].push(callback);
    } else {
      this.eventMap[eventName] = [callback];
    }
    return {
      unsubscribe: () => {
        // Find the event and remove the callback from the array
        this.eventMap[eventName] = this.eventMap[eventName].filter(
          (cb) => cb !== callback,
        );

        // Optional: Remove the event if no more callbacks are left
        if (this.eventMap[eventName].length === 0) {
          delete this.eventMap[eventName];
        }
      },
    };
  }

  emit(eventName: string, args: any[] = []): any[] {
    let result = [];
    if (!(eventName in this.eventMap)) {
      return result;
    }

    // console.log(this.eventMap)
    for (const cb of this.eventMap[eventName]) {
      // args.forEach((arg)=>console.log(typeof(arg)))
      result.push(cb(...args));
    }

    return result;
  }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */
