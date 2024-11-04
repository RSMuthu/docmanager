import Toolbar from '@mui/material/Toolbar'
import AppBar from '@mui/material/AppBar'
import Typography from '@mui/material/Typography'
import Container from '@mui/material/Container'
import { lazy } from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import { SWRConfig } from 'swr'

const Page404 = lazy(() => import('../../Pages/Page404'))
const DndBoard = lazy(() => import('../../Pages/DndBoard'))

const App = () => {
  return (
    <SWRConfig 
      value={{
        fetcher: (resource, init) => fetch(resource, init).then(res => res.json())
      }}
    >
    <Router>
      <AppBar component="nav" position="fixed">
        <Toolbar>
          <Typography variant="h6">Doc Manager</Typography>
        </Toolbar>
      </AppBar>
      <Container>
      <Routes>
        <Route path='' element={<DndBoard />} />
        <Route path="*" element={<Page404 />} />
      </Routes>
      </Container>
    </Router>
    </SWRConfig>
  )
}

export default App