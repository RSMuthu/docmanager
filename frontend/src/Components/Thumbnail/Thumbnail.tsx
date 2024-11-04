import Box from '@mui/material/Box'
import Grid from '@mui/material/Grid2'
import Modal from '@mui/material/Modal'
import Paper from '@mui/material/Paper'
import Typography from '@mui/material/Typography'

import { useState } from 'react';

interface Thumbnail {
  title: string;
  type: string;
  position: number;
}

interface ThumbnailListProps {
    thumbnails: Thumbnail[];
}

const Thumbnail = () => {
  const url = "https://media.istockphoto.com/id/1284671318/photo/meadows-in-the-snow-peak-mountains-of-himalaya.jpg?s=1024x1024&w=is&k=20&c=r-dL9kirCzRqWZHlkKOf3y4IS0rI8EmYZKI3ytTo_Iw="
  return (
    <Paper elevation={6}>
      <img src={url} alt="Thumbnail missing" style={{width: "100%"}} />
    </Paper>
  )
}
  
const ThumbnailList: React.FC<ThumbnailListProps> = ({ thumbnails }) => {
  const [selected, setSelected] = useState<number | undefined>()

  const modalBoxStyle = {
    position: 'absolute',
    top: '50%',
    left: '50%',
    transform: 'translate(-50%, -50%)',
    width: 750,
    bgcolor: 'background.paper',
    border: '2px solid #000',
    boxShadow: 24,
    p: 4,
  }

  return <>
    <Grid container spacing={2}>
      <Grid size={12} />
      {thumbnails.map((thumbnail, index) => (
        <Grid size={4} key={index} onClick={() => setSelected(index)} >
          <Thumbnail />
        </Grid>
      ))}
    </Grid>

    {/* modal for  displaying image selection */}
    <Modal
      open={selected !== undefined ? true : false}
      onClose={() => setSelected(undefined) }
    >
      <Box sx={modalBoxStyle}>
        {selected !== undefined && (
          <>
            <Typography id="thumbnail-title" variant="h6" component="h2">
              {thumbnails[selected].title}
            </Typography>
            <Thumbnail />
            <Typography id="thumbnail-title" sx={{ mt: 2 }}>
              {thumbnails[selected].type}
            </Typography>
          </>
        )}
      </Box>
    </Modal>
  </>
};

export default ThumbnailList