import Skeleton from "@mui/material/Skeleton";
import Grid from '@mui/material/Grid2';

export default function SkeletonLoading() {
    return <>
        <Grid container spacing={1}>
            <Grid size={5} />
            <Grid size={12}>
                <Skeleton height={14} />
            </Grid>
            <Grid size={12}>
                <Skeleton height={14} />
            </Grid>
            <Grid size={4}>
                <Skeleton height={100} />
            </Grid>
            <Grid size={8}>
                <Skeleton height={100} />
            </Grid>

            <Grid size={12}>
                <Skeleton height={150} />
            </Grid>
            <Grid size={12}>
                <Skeleton height={14} />
            </Grid>

            <Grid size={3}>
                <Skeleton height={100} />
            </Grid>
            <Grid size={3}>
                <Skeleton height={100} />
            </Grid>
            <Grid size={3}>
                <Skeleton height={100} />
            </Grid>
            <Grid size={3}>
                <Skeleton height={100} />
            </Grid>
        </Grid>
    </>
}