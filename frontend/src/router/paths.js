/**
 * Define all of your application routes here
 * for more information on routes, see the
 * official documentation https://router.vuejs.org/en/
 */
export default [
  {
    path: '/dashboard',
    // Relative to /src/views
    name: 'Dashboard',
    view: 'Dashboard',
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/DashStudent',
    // Relative to /src/views
    name: 'Dashboard',
    view: 'DashStudent',
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/home',
    // Relative to /src/views
    view: 'Home',
    name: 'Home'
  },
  {
    path: '/courses_enrolled',
    view: 'EnrolledCourses',
    name: 'Your Courses'
  },
  {
    path: '/feedback',
    view: 'Feedback',
    name: 'Feedback',
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/user-profile',
    name: 'User Profile',
    view: 'UserProfile',
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/table-list',
    name: 'Table List',
    view: 'TableList'
  },
  {
    path: '/typography',
    view: 'Typography'
  },
  {
    path: '/icons',
    view: 'Icons'
  },
  {
    path: '/maps',
    view: 'Maps'
  },
  {
    path: '/notifications',
    view: 'Notifications'
  },
  {
    path: '/calendar',
    view: 'Calendar'
  },
  {
    path: '/upgrade',
    name: 'Upgrade to PRO',
    view: 'Upgrade'
  },
  {
    path: '/course-structure/:id',
    name: 'Course Structure',
    view: 'CourseStructure'
  },
  {
    path: '/attendance/:id',
    name: 'Attendance',
    view: 'Attendance'
  },
  {
    path: '/attendance/:course_id/:roll_number',
    name: 'AttendanceInfo',
    view: 'AttendanceInfo'
  },
  {
    path: '/QuizList',
    name: 'QuizList',
    view: 'QuizList'
  },
  {
    path: '/CreateQuiz',
    name: 'CreateQuiz',
    view: 'CreateQuiz'
  },
  {
    path: '/quizes/:id',
    name: 'Quiz',
    view: 'Quiz'
  },
  {
    path: '/quizes/create-new',
    name: 'Create New Quiz',
    view: 'CreateNewQuiz'
  },
  {
    path: '/resources:id',
    name: 'Resources',
    view: 'Resources'
  },
  {
    path: '/courses',
    name: 'CourseList',
    view: 'CourseList',
    meta: {
      requiresAuth: true,
      requiresAuthInstructor: true
    }
  },
  {
    path: '/studentList',
    name: 'Student Statistics',
    view: 'studentList',
    meta: {
      requiresAuth: true,
      requiresAuthInstructor: true
    }
  },
  {
    path: '/test',
    name: 'Test',
    view: 'test'
  }


]
