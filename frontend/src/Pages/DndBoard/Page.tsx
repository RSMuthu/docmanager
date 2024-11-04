import Thumbnail from "../../Components/Thumbnail"
import Skeleton from "../../Components/SkeletonLoading"
import Box from "@mui/material/Box"
import Toolbar from "@mui/material/Toolbar"
import useSwr from "swr"
import Modal from "@mui/material/Modal"
import { Typography } from "@mui/material"

const Page = () => {
    const { data, isLoading, error } = useSwr('http://127.0.0.1:8000/api/v1/docs');
    const modalBoxStyle = {
        position: 'absolute',
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        width: 340,
        bgcolor: 'background.paper',
        border: '2px solid #000',
        boxShadow: 24,
        p: 4,
    }

    // Handle loading and error states
    if (isLoading) return <Box component="main"><Toolbar/><Skeleton/></Box>;
    if (error) return (
        <Modal
          open
          disableEscapeKeyDown
          disableEnforceFocus
        >
            <Box sx={modalBoxStyle}>
                <Typography id="thumbnail-title" variant="h6" component="h2">
                    Error
                </Typography>
                <Typography id="thumbnail-title" sx={{ mt: 2 }}>
                    Facing error when getting data from the server
                </Typography>
            </Box>
        </Modal>
    )
    
    return <Box component="main">
        <Toolbar/>
        {
            data.data.length === 0 
            ? <>
                {"No Data found"}
            </>
            : <Thumbnail thumbnails={data.data} />
        }
    </Box>

}

export default Page