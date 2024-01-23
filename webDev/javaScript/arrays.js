// Used to store multiple values in a single variable

const courses = ['BE', 'phy', 'CompSci', 'ET']
console.log(courses)

// we can access an element inside an array using the index
console.log(courses[0])

courses[0] = 'CMB'
console.log(courses)
console.log(courses.toString())

console.log(typeof courses)

courses.push('prob')
courses.pop()
console.log(courses)